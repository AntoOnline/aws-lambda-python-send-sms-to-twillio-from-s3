# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UsAppToPersonUsecaseList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, messaging_service_sid):
        """
        Initialize the UsAppToPersonUsecaseList

        :param Version version: Version that contains the resource
        :param messaging_service_sid: The unique string that identifies the resource

        :returns: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseList
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseList
        """
        super(UsAppToPersonUsecaseList, self).__init__(version)

        # Path Solution
        self._solution = {'messaging_service_sid': messaging_service_sid, }
        self._uri = '/Services/{messaging_service_sid}/Compliance/Usa2p/Usecases'.format(**self._solution)

    def fetch(self):
        """
        Fetch the UsAppToPersonUsecaseInstance

        :returns: The fetched UsAppToPersonUsecaseInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UsAppToPersonUsecaseInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution['messaging_service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UsAppToPersonUsecaseList>'


class UsAppToPersonUsecasePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the UsAppToPersonUsecasePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param messaging_service_sid: The unique string that identifies the resource

        :returns: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecasePage
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecasePage
        """
        super(UsAppToPersonUsecasePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UsAppToPersonUsecaseInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseInstance
        """
        return UsAppToPersonUsecaseInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution['messaging_service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UsAppToPersonUsecasePage>'


class UsAppToPersonUsecaseInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, messaging_service_sid):
        """
        Initialize the UsAppToPersonUsecaseInstance

        :returns: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseInstance
        """
        super(UsAppToPersonUsecaseInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'us_app_to_person_usecases': payload.get('us_app_to_person_usecases'), }

        # Context
        self._context = None
        self._solution = {'messaging_service_sid': messaging_service_sid, }

    @property
    def us_app_to_person_usecases(self):
        """
        :returns: Human readable A2P Use Case details
        :rtype: list[dict]
        """
        return self._properties['us_app_to_person_usecases']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UsAppToPersonUsecaseInstance>'