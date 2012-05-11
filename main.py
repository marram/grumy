#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import settings
import json
import logging
import urllib
from google.appengine.api import urlfetch
import base64

resource_to_rest_verb = dict(task="tasks", story="stories")

def fetch_from_scrumy(resource, id):
    auth_string = 'Basic ' + base64.encodestring("%s:%s" % (settings.SCRUMY_PROJECT, settings.SCRUMY_PASSWORD))
    headers= {'AUTHORIZATION' : auth_string}
    url = settings.SCRUMY_ENDPOINT + "%s/%s.json" % (resource_to_rest_verb.get(resource), id)
    logging.info("fetching from scrumy")
    logging.info("url is %s" % url)
    content = urlfetch.fetch(url=url, method=urlfetch.GET, headers=headers).content
    return json.loads(content).get(resource)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # path = os.path.join(os.path.dirname(__file__), "templates", "landing.html")
        # template_values = {}
        # self.response.out.write(template.render(path, template_values))
        return self.post()

    def post(self):
        """ Handles the posts from Scrumy.
        """
        self.action = str(self.request.get("action")).lower()
        func = getattr(self, "handle_"+self.action, None)
        if func:
            return func()

    def render_envelope(self):
        path = os.path.join(os.path.dirname(__file__), "templates", "base_grove_dict.json")
        template_values = settings.ALL
        template_string = template.render(path, template_values)
        template_dict = json.loads(template_string)
        return template_dict


    def render_action(self):
        path = os.path.join(os.path.dirname(__file__), "templates", self.action+".html")
        template_values = dict()
        template_values.update(self.request.GET)
        template_values.update(self.request.POST)
        data = json.loads(self.request.POST.get("data", "{}"))
        # Fetch any id
        if template_values.get("id", None):
            try:
                data.update(fetch_from_scrumy(template_values.get(u"resource"), template_values.get(u"id")))
            except Exception, e:
                logging.error(e)

        if template_values.get("story_id", None):
            try:
                data.update(dict(story=fetch_from_scrumy("story", template_values.get(u"story_id"))))
            except Exception, e:
                logging.error(e)

        template_values.update(data)
        logging.info(template_values)
        template_string = template.render(path, template_values)
        return template_string

    def default(self):
        envelope = self.render_envelope()
        message = str(self.render_action()).strip()
        envelope.update(dict(message=message))
        logging.info(str(envelope))
        return envelope

    def post_to_grove(self, data):
        logging.info("posting to grove ...")
        logging.info(data)
        form_data = urllib.urlencode(data)
        result = urlfetch.fetch(url=settings.GROVE_ENDPOINT,
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'})
        logging.info(result.content)

    def handle_create(self):
        """ A resource (such as a task, a story or a sprint) is created on Scrumy.

        When a resource is created, a POST will be sent to the webhook with the following parameters:

        time: The time the resource was created in seconds since the epoch
        action: create
        resource: Will be one of task, story, sprint
        data: A JSON string representing the created resource. Looks something like this:

        {title:Test create,&quot;id&quot;:1527293,&quot;story_id&quot;:418611,&quot;seq&quot;:0,&quot;state&quot;:&quot;todo&quot;}
        """
        envelope = self.default()
        self.post_to_grove(envelope)

    def handle_update(self):
        """ A resource (such as a task, a story or a sprint) is updated on Scrumy.

        When a resource is updated, a POST will be sent to the webhook with the following parameters:

        time: The time the resource was created in seconds since the epoch
        action: update
        resource: Will be one of task, story, sprint
        id: The id of the resource being updated
        data: A JSON string representing the changes. This will be in the form of {field: [original value, new value]}
        """
        envelope = self.default()
        self.post_to_grove(envelope)

    def handle_destroy(self):
        """ A resource (such as a task, a story or a sprint) is destroyed on Scrumy.

        When a resource is deleted, a POST will be sent to the webhook with the following parameters:

        time: The time the resource was created in seconds since the epoch
        action: destroy
        resource: Will be one of task, story, sprint
        id: The id of the deleted resource
        """
        pass

    def handle_order_tasks(self):
        """
        In addition to the standard updates, sprints and stories have special update actions for reordering of stories and tasks. In these cases, the POST will be like the following:

        time: The time the resource was created in seconds since the epoch
        action: order_tasks
        resource: story
        id: The id of the story whose tasks have been reordered
        data: A JSON string containing an array of task ids representing the order of the tasks.
        """
        pass

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
