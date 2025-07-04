"""
This type stub file was generated by pyright.
"""

"""
The models defined in this file represent the resource JSON description
format and provide a layer of abstraction from the raw JSON. The advantages
of this are:

* Pythonic interface (e.g. ``action.request.operation``)
* Consumers need not change for minor JSON changes (e.g. renamed field)

These models are used both by the resource factory to generate resource
classes as well as by the documentation generator.
"""
logger = ...
class Identifier:
    """
    A resource identifier, given by its name.

    :type name: string
    :param name: The name of the identifier
    """
    def __init__(self, name, member_name=...) -> None:
        ...
    


class Action:
    """
    A service operation action.

    :type name: string
    :param name: The name of the action
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, name, definition, resource_defs) -> None:
        ...
    


class DefinitionWithParams:
    """
    An item which has parameters exposed via the ``params`` property.
    A request has an operation and parameters, while a waiter has
    a name, a low-level waiter name and parameters.

    :type definition: dict
    :param definition: The JSON definition
    """
    def __init__(self, definition) -> None:
        ...
    
    @property
    def params(self): # -> list[Any]:
        """
        Get a list of auto-filled parameters for this request.

        :type: list(:py:class:`Parameter`)
        """
        ...
    


class Parameter:
    """
    An auto-filled parameter which has a source and target. For example,
    the ``QueueUrl`` may be auto-filled from a resource's ``url`` identifier
    when making calls to ``queue.receive_messages``.

    :type target: string
    :param target: The destination parameter name, e.g. ``QueueUrl``
    :type source_type: string
    :param source_type: Where the source is defined.
    :type source: string
    :param source: The source name, e.g. ``Url``
    """
    def __init__(self, target, source, name=..., path=..., value=..., **kwargs) -> None:
        ...
    


class Request(DefinitionWithParams):
    """
    A service operation action request.

    :type definition: dict
    :param definition: The JSON definition
    """
    def __init__(self, definition) -> None:
        ...
    


class Waiter(DefinitionWithParams):
    """
    An event waiter specification.

    :type name: string
    :param name: Name of the waiter
    :type definition: dict
    :param definition: The JSON definition
    """
    PREFIX = ...
    def __init__(self, name, definition) -> None:
        ...
    


class ResponseResource:
    """
    A resource response to create after performing an action.

    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, definition, resource_defs) -> None:
        ...
    
    @property
    def identifiers(self): # -> list[Any]:
        """
        A list of resource identifiers.

        :type: list(:py:class:`Identifier`)
        """
        ...
    
    @property
    def model(self): # -> ResourceModel:
        """
        Get the resource model for the response resource.

        :type: :py:class:`ResourceModel`
        """
        ...
    


class Collection(Action):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    @property
    def batch_actions(self): # -> list[Any]:
        """
        Get a list of batch actions supported by the resource type
        contained in this action. This is a shortcut for accessing
        the same information through the resource model.

        :rtype: list(:py:class:`Action`)
        """
        ...
    


class ResourceModel:
    """
    A model representing a resource, defined via a JSON description
    format. A resource has identifiers, attributes, actions,
    sub-resources, references and collections. For more information
    on resources, see :ref:`guide_resources`.

    :type name: string
    :param name: The name of this resource, e.g. ``sqs`` or ``Queue``
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """
    def __init__(self, name, definition, resource_defs) -> None:
        ...
    
    def load_rename_map(self, shape=...): # -> None:
        """
        Load a name translation map given a shape. This will set
        up renamed values for any collisions, e.g. if the shape,
        an action, and a subresource all are all named ``foo``
        then the resource will have an action ``foo``, a subresource
        named ``Foo`` and a property named ``foo_attribute``.
        This is the order of precedence, from most important to
        least important:

        * Load action (resource.load)
        * Identifiers
        * Actions
        * Subresources
        * References
        * Collections
        * Waiters
        * Attributes (shape members)

        Batch actions are only exposed on collections, so do not
        get modified here. Subresources use upper camel casing, so
        are unlikely to collide with anything but other subresources.

        Creates a structure like this::

            renames = {
                ('action', 'id'): 'id_action',
                ('collection', 'id'): 'id_collection',
                ('attribute', 'id'): 'id_attribute'
            }

            # Get the final name for an action named 'id'
            name = renames.get(('action', 'id'), 'id')

        :type shape: botocore.model.Shape
        :param shape: The underlying shape for this resource.
        """
        ...
    
    def get_attributes(self, shape): # -> dict[Any, Any]:
        """
        Get a dictionary of attribute names to original name and shape
        models that represent the attributes of this resource. Looks
        like the following:

            {
                'some_name': ('SomeName', <Shape...>)
            }

        :type shape: botocore.model.Shape
        :param shape: The underlying shape for this resource.
        :rtype: dict
        :return: Mapping of resource attributes.
        """
        ...
    
    @property
    def identifiers(self): # -> list[Any]:
        """
        Get a list of resource identifiers.

        :type: list(:py:class:`Identifier`)
        """
        ...
    
    @property
    def load(self): # -> Action:
        """
        Get the load action for this resource, if it is defined.

        :type: :py:class:`Action` or ``None``
        """
        ...
    
    @property
    def actions(self): # -> list[Any]:
        """
        Get a list of actions for this resource.

        :type: list(:py:class:`Action`)
        """
        ...
    
    @property
    def batch_actions(self): # -> list[Any]:
        """
        Get a list of batch actions for this resource.

        :type: list(:py:class:`Action`)
        """
        ...
    
    @property
    def subresources(self): # -> list[Any]:
        """
        Get a list of sub-resources.

        :type: list(:py:class:`Action`)
        """
        ...
    
    @property
    def references(self): # -> list[Any]:
        """
        Get a list of reference resources.

        :type: list(:py:class:`Action`)
        """
        ...
    
    @property
    def collections(self): # -> list[Any]:
        """
        Get a list of collections for this resource.

        :type: list(:py:class:`Collection`)
        """
        ...
    
    @property
    def waiters(self): # -> list[Any]:
        """
        Get a list of waiters for this resource.

        :type: list(:py:class:`Waiter`)
        """
        ...
    


