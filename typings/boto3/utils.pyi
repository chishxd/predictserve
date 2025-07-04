"""
This type stub file was generated by pyright.
"""

_ServiceContext = ...
class ServiceContext(_ServiceContext):
    """Provides important service-wide, read-only information about a service

    :type service_name: str
    :param service_name: The name of the service

    :type service_model: :py:class:`botocore.model.ServiceModel`
    :param service_model: The model of the service.

    :type service_waiter_model: :py:class:`botocore.waiter.WaiterModel` or
        a waiter model-like object such as
        :py:class:`boto3.utils.LazyLoadedWaiterModel`
    :param service_waiter_model: The waiter model of the service.

    :type resource_json_definitions: dict
    :param resource_json_definitions: The loaded json models of all resource
        shapes for a service. It is equivalient of loading a
        ``resource-1.json`` and retrieving the value at the key "resources".
    """
    ...


def import_module(name): # -> ModuleType:
    """Import module given a name.

    Does not support relative imports.

    """
    ...

def lazy_call(full_name, **kwargs): # -> Callable[..., Any]:
    ...

def inject_attribute(class_attributes, name, value): # -> None:
    ...

class LazyLoadedWaiterModel:
    """A lazily loaded waiter model

    This does not load the service waiter model until an attempt is made
    to retrieve the waiter model for a specific waiter. This is helpful
    in docstring generation where we do not need to actually need to grab
    the waiter-2.json until it is accessed through a ``get_waiter`` call
    when the docstring is generated/accessed.
    """
    def __init__(self, bc_session, service_name, api_version) -> None:
        ...
    
    def get_waiter(self, waiter_name):
        ...
    


