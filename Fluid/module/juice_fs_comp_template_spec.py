# -*- coding: utf-8 -*-


import pprint

import six
from fluid.configuration import Configuration


class JuiceFSCompTemplateSpec(object):
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
        'enabled': 'bool',
        'env': 'list[V1EnvVar]',
        'node_selector': 'dict(str, str)',
        'ports': 'list[V1ContainerPort]',
        'replicas': 'int',
        'resources': 'V1ResourceRequirements'
    }

    attribute_map = {
        'enabled': 'enabled',
        'env': 'env',
        'node_selector': 'nodeSelector',
        'ports': 'ports',
        'replicas': 'replicas',
        'resources': 'resources'
    }

    def __init__(self, enabled=None, env=None, node_selector=None, ports=None, replicas=None, resources=None, _configuration=None):  # noqa: E501
        """JuiceFSCompTemplateSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._env = None
        self._node_selector = None
        self._ports = None
        self._replicas = None
        self._resources = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if env is not None:
            self.env = env
        if node_selector is not None:
            self.node_selector = node_selector
        if ports is not None:
            self.ports = ports
        if replicas is not None:
            self.replicas = replicas
        if resources is not None:
            self.resources = resources

    @property
    def enabled(self):
        """Gets the enabled of this JuiceFSCompTemplateSpec.  # noqa: E501

        Enabled or Disabled for the components.  # noqa: E501

        :return: The enabled of this JuiceFSCompTemplateSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this JuiceFSCompTemplateSpec.

        Enabled or Disabled for the components.  # noqa: E501

        :param enabled: The enabled of this JuiceFSCompTemplateSpec.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def env(self):
        """Gets the env of this JuiceFSCompTemplateSpec.  # noqa: E501

        Environment variables that will be used by JuiceFS component.  # noqa: E501

        :return: The env of this JuiceFSCompTemplateSpec.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this JuiceFSCompTemplateSpec.

        Environment variables that will be used by JuiceFS component.  # noqa: E501

        :param env: The env of this JuiceFSCompTemplateSpec.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def node_selector(self):
        """Gets the node_selector of this JuiceFSCompTemplateSpec.  # noqa: E501

        NodeSelector is a selector  # noqa: E501

        :return: The node_selector of this JuiceFSCompTemplateSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this JuiceFSCompTemplateSpec.

        NodeSelector is a selector  # noqa: E501

        :param node_selector: The node_selector of this JuiceFSCompTemplateSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def ports(self):
        """Gets the ports of this JuiceFSCompTemplateSpec.  # noqa: E501

        Ports used by JuiceFS  # noqa: E501

        :return: The ports of this JuiceFSCompTemplateSpec.  # noqa: E501
        :rtype: list[V1ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this JuiceFSCompTemplateSpec.

        Ports used by JuiceFS  # noqa: E501

        :param ports: The ports of this JuiceFSCompTemplateSpec.  # noqa: E501
        :type: list[V1ContainerPort]
        """

        self._ports = ports

    @property
    def replicas(self):
        """Gets the replicas of this JuiceFSCompTemplateSpec.  # noqa: E501

        Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster  # noqa: E501

        :return: The replicas of this JuiceFSCompTemplateSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this JuiceFSCompTemplateSpec.

        Replicas is the desired number of replicas of the given template. If unspecified, defaults to 1. replicas is the min replicas of dataset in the cluster  # noqa: E501

        :param replicas: The replicas of this JuiceFSCompTemplateSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def resources(self):
        """Gets the resources of this JuiceFSCompTemplateSpec.  # noqa: E501

        Resources that will be requested by the JuiceFS component.  # noqa: E501

        :return: The resources of this JuiceFSCompTemplateSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this JuiceFSCompTemplateSpec.

        Resources that will be requested by the JuiceFS component.  # noqa: E501

        :param resources: The resources of this JuiceFSCompTemplateSpec.  # noqa: E501
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
        if issubclass(JuiceFSCompTemplateSpec, dict):
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
        if not isinstance(other, JuiceFSCompTemplateSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JuiceFSCompTemplateSpec):
            return True

        return self.to_dict() != other.to_dict()
