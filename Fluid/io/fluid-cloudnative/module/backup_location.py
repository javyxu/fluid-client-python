# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BackupLocation(object):
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
        'node_name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'node_name': 'nodeName',
        'path': 'path'
    }

    def __init__(self, node_name=None, path=None):  # noqa: E501
        """BackupLocation - a model defined in Swagger"""  # noqa: E501

        self._node_name = None
        self._path = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        if path is not None:
            self.path = path

    @property
    def node_name(self):
        """Gets the node_name of this BackupLocation.  # noqa: E501

        NodeName describes the nodeName of backup if Path is in the form of local://subpath  # noqa: E501

        :return: The node_name of this BackupLocation.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this BackupLocation.

        NodeName describes the nodeName of backup if Path is in the form of local://subpath  # noqa: E501

        :param node_name: The node_name of this BackupLocation.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def path(self):
        """Gets the path of this BackupLocation.  # noqa: E501

        Path describes the path of backup, in the form of local:///absolutePath or pvc://<pvcName>/subpath  # noqa: E501

        :return: The path of this BackupLocation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BackupLocation.

        Path describes the path of backup, in the form of local:///absolutePath or pvc://<pvcName>/subpath  # noqa: E501

        :param path: The path of this BackupLocation.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(BackupLocation, dict):
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
        if not isinstance(other, BackupLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
