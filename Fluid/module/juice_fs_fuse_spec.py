# -*- coding: utf-8 -*-


import pprint

import six
from fluid.configuration import Configuration


class JuiceFSFuseSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'clean_policy': 'str',
        'env': 'list[V1EnvVar]',
        '_global': 'bool',
        'image': 'str',
        'image_pull_policy': 'str',
        'image_tag': 'str',
        'node_selector': 'dict(str, str)',
        'resources': 'V1ResourceRequirements'
    }

    attribute_map = {
        'clean_policy': 'cleanPolicy',
        'env': 'env',
        '_global': 'global',
        'image': 'image',
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag',
        'node_selector': 'nodeSelector',
        'resources': 'resources'
    }

    def __init__(self, clean_policy=None, env=None, _global=None, image=None, image_pull_policy=None, image_tag=None, node_selector=None, resources=None, _configuration=None):  # noqa: E501
        """JuiceFSFuseSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clean_policy = None
        self._env = None
        self.__global = None
        self._image = None
        self._image_pull_policy = None
        self._image_tag = None
        self._node_selector = None
        self._resources = None
        self.discriminator = None

        if clean_policy is not None:
            self.clean_policy = clean_policy
        if env is not None:
            self.env = env
        if _global is not None:
            self._global = _global
        if image is not None:
            self.image = image
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag
        if node_selector is not None:
            self.node_selector = node_selector
        if resources is not None:
            self.resources = resources

    @property
    def clean_policy(self):
        """Gets the clean_policy of this JuiceFSFuseSpec.  # noqa: E501

        CleanPolicy decides when to clean Juicefs Fuse pods. Currently fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand  # noqa: E501

        :return: The clean_policy of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._clean_policy

    @clean_policy.setter
    def clean_policy(self, clean_policy):
        """Sets the clean_policy of this JuiceFSFuseSpec.

        CleanPolicy decides when to clean Juicefs Fuse pods. Currently fluid supports two policies: OnDemand and OnRuntimeDeleted OnDemand cleans fuse pod once th fuse pod on some node is not needed OnRuntimeDeleted cleans fuse pod only when the cache runtime is deleted Defaults to OnDemand  # noqa: E501

        :param clean_policy: The clean_policy of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._clean_policy = clean_policy

    @property
    def env(self):
        """Gets the env of this JuiceFSFuseSpec.  # noqa: E501

        Environment variables that will be used by JuiceFS Fuse  # noqa: E501

        :return: The env of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this JuiceFSFuseSpec.

        Environment variables that will be used by JuiceFS Fuse  # noqa: E501

        :param env: The env of this JuiceFSFuseSpec.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def _global(self):
        """Gets the _global of this JuiceFSFuseSpec.  # noqa: E501

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :return: The _global of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this JuiceFSFuseSpec.

        If the fuse client should be deployed in global mode, otherwise the affinity should be considered  # noqa: E501

        :param _global: The _global of this JuiceFSFuseSpec.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def image(self):
        """Gets the image of this JuiceFSFuseSpec.  # noqa: E501

        Image for JuiceFS fuse  # noqa: E501

        :return: The image of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this JuiceFSFuseSpec.

        Image for JuiceFS fuse  # noqa: E501

        :param image: The image of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this JuiceFSFuseSpec.  # noqa: E501

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :return: The image_pull_policy of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this JuiceFSFuseSpec.

        One of the three policies: `Always`, `IfNotPresent`, `Never`  # noqa: E501

        :param image_pull_policy: The image_pull_policy of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        """Gets the image_tag of this JuiceFSFuseSpec.  # noqa: E501

        Image for JuiceFS fuse  # noqa: E501

        :return: The image_tag of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this JuiceFSFuseSpec.

        Image for JuiceFS fuse  # noqa: E501

        :param image_tag: The image_tag of this JuiceFSFuseSpec.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def node_selector(self):
        """Gets the node_selector of this JuiceFSFuseSpec.  # noqa: E501

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :return: The node_selector of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this JuiceFSFuseSpec.

        NodeSelector is a selector which must be true for the fuse client to fit on a node, this option only effect when global is enabled  # noqa: E501

        :param node_selector: The node_selector of this JuiceFSFuseSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def resources(self):
        """Gets the resources of this JuiceFSFuseSpec.  # noqa: E501

        Resources that will be requested by JuiceFS Fuse.  # noqa: E501

        :return: The resources of this JuiceFSFuseSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this JuiceFSFuseSpec.

        Resources that will be requested by JuiceFS Fuse.  # noqa: E501

        :param resources: The resources of this JuiceFSFuseSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JuiceFSFuseSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JuiceFSFuseSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JuiceFSFuseSpec):
            return True

        return self.to_dict() != other.to_dict()
