# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class FactorList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, identity):
        """
        Initialize the FactorList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorList
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorList
        """
        super(FactorList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'identity': identity, }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Factors'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FactorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.factor.FactorInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FactorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.factor.FactorInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FactorInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return FactorPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FactorInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FactorPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FactorContext

        :param sid: A string that uniquely identifies this Factor.

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorContext
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        return FactorContext(
            self._version,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a FactorContext

        :param sid: A string that uniquely identifies this Factor.

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorContext
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        return FactorContext(
            self._version,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.FactorList>'


class FactorPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the FactorPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorPage
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorPage
        """
        super(FactorPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FactorInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.FactorPage>'


class FactorContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, identity, sid):
        """
        Initialize the FactorContext

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity
        :param sid: A string that uniquely identifies this Factor.

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorContext
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        super(FactorContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'identity': identity, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Factors/{sid}'.format(**self._solution)

    def delete(self):
        """
        Deletes the FactorInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the FactorInstance

        :returns: The fetched FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid'],
        )

    def update(self, auth_payload=values.unset, friendly_name=values.unset,
               config_notification_token=values.unset,
               config_sdk_version=values.unset, config_time_step=values.unset,
               config_skew=values.unset, config_code_length=values.unset,
               config_alg=values.unset):
        """
        Update the FactorInstance

        :param unicode auth_payload: Optional payload to verify the Factor for the first time
        :param unicode friendly_name: The friendly name of this Factor
        :param unicode config_notification_token: For APN, the device token. For FCM the registration token
        :param unicode config_sdk_version: The Verify Push SDK version used to configure the factor
        :param unicode config_time_step: How often, in seconds, are TOTP codes generated
        :param unicode config_skew: The number of past and future time-steps valid at a given time
        :param unicode config_code_length: Number of digits for generated TOTP codes
        :param FactorInstance.TotpAlgorithms config_alg: The algorithm used to derive the TOTP codes

        :returns: The updated FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        data = values.of({
            'AuthPayload': auth_payload,
            'FriendlyName': friendly_name,
            'Config.NotificationToken': config_notification_token,
            'Config.SdkVersion': config_sdk_version,
            'Config.TimeStep': config_time_step,
            'Config.Skew': config_skew,
            'Config.CodeLength': config_code_length,
            'Config.Alg': config_alg,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.FactorContext {}>'.format(context)


class FactorInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class FactorStatuses(object):
        UNVERIFIED = "unverified"
        VERIFIED = "verified"

    class FactorTypes(object):
        PUSH = "push"
        TOTP = "totp"

    class NotificationPlatforms(object):
        APN = "apn"
        FCM = "fcm"

    class TotpAlgorithms(object):
        SHA1 = "sha1"
        SHA256 = "sha256"
        SHA512 = "sha512"

    def __init__(self, version, payload, service_sid, identity, sid=None):
        """
        Initialize the FactorInstance

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        super(FactorInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_sid': payload.get('entity_sid'),
            'identity': payload.get('identity'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'factor_type': payload.get('factor_type'),
            'config': payload.get('config'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'identity': identity,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FactorContext for this FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        if self._context is None:
            self._context = FactorContext(
                self._version,
                service_sid=self._solution['service_sid'],
                identity=self._solution['identity'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Factor.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def entity_sid(self):
        """
        :returns: Entity Sid.
        :rtype: unicode
        """
        return self._properties['entity_sid']

    @property
    def identity(self):
        """
        :returns: Unique external identifier of the Entity
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def date_created(self):
        """
        :returns: The date this Factor was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Factor was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def status(self):
        """
        :returns: The Status of this Factor
        :rtype: FactorInstance.FactorStatuses
        """
        return self._properties['status']

    @property
    def factor_type(self):
        """
        :returns: The Type of this Factor
        :rtype: FactorInstance.FactorTypes
        """
        return self._properties['factor_type']

    @property
    def config(self):
        """
        :returns: Configurations for a `factor_type`.
        :rtype: dict
        """
        return self._properties['config']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def delete(self):
        """
        Deletes the FactorInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the FactorInstance

        :returns: The fetched FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        return self._proxy.fetch()

    def update(self, auth_payload=values.unset, friendly_name=values.unset,
               config_notification_token=values.unset,
               config_sdk_version=values.unset, config_time_step=values.unset,
               config_skew=values.unset, config_code_length=values.unset,
               config_alg=values.unset):
        """
        Update the FactorInstance

        :param unicode auth_payload: Optional payload to verify the Factor for the first time
        :param unicode friendly_name: The friendly name of this Factor
        :param unicode config_notification_token: For APN, the device token. For FCM the registration token
        :param unicode config_sdk_version: The Verify Push SDK version used to configure the factor
        :param unicode config_time_step: How often, in seconds, are TOTP codes generated
        :param unicode config_skew: The number of past and future time-steps valid at a given time
        :param unicode config_code_length: Number of digits for generated TOTP codes
        :param FactorInstance.TotpAlgorithms config_alg: The algorithm used to derive the TOTP codes

        :returns: The updated FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        return self._proxy.update(
            auth_payload=auth_payload,
            friendly_name=friendly_name,
            config_notification_token=config_notification_token,
            config_sdk_version=config_sdk_version,
            config_time_step=config_time_step,
            config_skew=config_skew,
            config_code_length=config_code_length,
            config_alg=config_alg,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.FactorInstance {}>'.format(context)
