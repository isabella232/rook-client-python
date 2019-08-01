"""
This file is automatically generated.
Do not modify.
"""

if False:
    from typing import List, Dict, Any, Optional

# Tricking mypy to think `_omit`'s type is NoneType
# To make us not add things like `Union[Optional[str], OmitType]`
NoneType = type(None)  
_omit = None  # type: NoneType
_omit = object()  # type: ignore

class Rados(object):
    def __init__(self,
                 pool=_omit,  # type: Optional[str]
                 namespace=_omit,  # type: Optional[str]
                 ):
        self.pool = pool  # type: ignore
        self.namespace = namespace  # type: ignore

    @property
    def pool(self):
        # type: () -> str
        if self._pool is _omit:
            raise AttributeError('pool not found')
        return self._pool
    
    @pool.setter
    def pool(self, new_val):
        # type: (Optional[str]) -> None
        self._pool = new_val
    
    @property
    def namespace(self):
        # type: () -> str
        if self._namespace is _omit:
            raise AttributeError('namespace not found')
        return self._namespace
    
    @namespace.setter
    def namespace(self, new_val):
        # type: (Optional[str]) -> None
        self._namespace = new_val

    def to_json(self):
        res = {
            'pool': self._pool,
            'namespace': self._namespace,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Rados]
        return cls(
            pool=data.get('pool', _omit),
            namespace=data.get('namespace', _omit),
        )


class Server(object):
    def __init__(self,
                 active=_omit,  # type: Optional[int]
                 annotations=_omit,  # type: Optional[Any]
                 placement=_omit,  # type: Optional[Any]
                 resources=_omit,  # type: Optional[Any]
                 ):
        self.active = active  # type: ignore
        self.annotations = annotations  # type: ignore
        self.placement = placement  # type: ignore
        self.resources = resources  # type: ignore

    @property
    def active(self):
        # type: () -> int
        if self._active is _omit:
            raise AttributeError('active not found')
        return self._active
    
    @active.setter
    def active(self, new_val):
        # type: (Optional[int]) -> None
        self._active = new_val
    
    @property
    def annotations(self):
        # type: () -> Any
        if self._annotations is _omit:
            raise AttributeError('annotations not found')
        return self._annotations
    
    @annotations.setter
    def annotations(self, new_val):
        # type: (Optional[Any]) -> None
        self._annotations = new_val
    
    @property
    def placement(self):
        # type: () -> Any
        if self._placement is _omit:
            raise AttributeError('placement not found')
        return self._placement
    
    @placement.setter
    def placement(self, new_val):
        # type: (Optional[Any]) -> None
        self._placement = new_val
    
    @property
    def resources(self):
        # type: () -> Any
        if self._resources is _omit:
            raise AttributeError('resources not found')
        return self._resources
    
    @resources.setter
    def resources(self, new_val):
        # type: (Optional[Any]) -> None
        self._resources = new_val

    def to_json(self):
        res = {
            'active': self._active,
            'annotations': self._annotations,
            'placement': self._placement,
            'resources': self._resources,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Server]
        return cls(
            active=data.get('active', _omit),
            annotations=data.get('annotations', _omit),
            placement=data.get('placement', _omit),
            resources=data.get('resources', _omit),
        )


class Spec(object):
    def __init__(self,
                 rados=_omit,  # type: Optional[Rados]
                 server=_omit,  # type: Optional[Server]
                 ):
        self.rados = rados  # type: ignore
        self.server = server  # type: ignore

    @property
    def rados(self):
        # type: () -> Rados
        if self._rados is _omit:
            raise AttributeError('rados not found')
        return self._rados
    
    @rados.setter
    def rados(self, new_val):
        # type: (Optional[Rados]) -> None
        self._rados = new_val
    
    @property
    def server(self):
        # type: () -> Server
        if self._server is _omit:
            raise AttributeError('server not found')
        return self._server
    
    @server.setter
    def server(self, new_val):
        # type: (Optional[Server]) -> None
        self._server = new_val

    def to_json(self):
        res = {
            'rados': self.rados.to_json() if self._rados is not _omit else self._rados,
            'server': self.server.to_json() if self._server is not _omit else self._server,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Spec
        return cls(
            rados=Rados.from_json(data['rados']) if 'rados' in data else _omit,
            server=Server.from_json(data['server']) if 'server' in data else _omit,
        )


class CephNFS(object):
    def __init__(self,
                 apiVersion,  # type: str
                 metadata,  # type: Any
                 spec,  # type: Spec
                 kind="CephNFS",  # type: str
                 ):
        self.apiVersion = apiVersion  # type: ignore
        self.metadata = metadata  # type: ignore
        self.spec = spec  # type: ignore
        self.kind = kind  # type: ignore

    @property
    def apiVersion(self):
        # type: () -> str
        if self._apiVersion is _omit:
            raise AttributeError('apiVersion not found')
        return self._apiVersion
    
    @apiVersion.setter
    def apiVersion(self, new_val):
        # type: (str) -> None
        self._apiVersion = new_val
    
    @property
    def kind(self):
        # type: () -> str
        if self._kind is _omit:
            raise AttributeError('kind not found')
        return self._kind
    
    @kind.setter
    def kind(self, new_val):
        # type: (str) -> None
        self._kind = new_val
    
    @property
    def metadata(self):
        # type: () -> Any
        if self._metadata is _omit:
            raise AttributeError('metadata not found')
        return self._metadata
    
    @metadata.setter
    def metadata(self, new_val):
        # type: (Any) -> None
        self._metadata = new_val
    
    @property
    def spec(self):
        # type: () -> Spec
        if self._spec is _omit:
            raise AttributeError('spec not found')
        return self._spec
    
    @spec.setter
    def spec(self, new_val):
        # type: (Spec) -> None
        self._spec = new_val

    def to_json(self):
        res = {
            'apiVersion': self._apiVersion,
            'kind': self._kind,
            'metadata': self._metadata,
            'spec': self.spec.to_json(),
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> CephNFS
        return cls(
            apiVersion=data['apiVersion'],
            kind=data['kind'],
            metadata=data['metadata'],
            spec=Spec.from_json(data['spec']),
        )
