"""
This type stub file was generated by pyright.
"""

from boto3.docs.base import NestedDocumenter

class SubResourceDocumenter(NestedDocumenter):
    def document_sub_resources(self, section): # -> None:
        ...
    


def document_sub_resource(section, resource_name, sub_resource_model, service_model, include_signature=...): # -> None:
    """Documents a resource action

    :param section: The section to write to

    :param resource_name: The name of the resource

    :param sub_resource_model: The model of the subresource

    :param service_model: The model of the service

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    ...

