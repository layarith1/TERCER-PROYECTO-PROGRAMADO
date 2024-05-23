from abc import ABC, abstractmethod

class EntityInterface(ABC):
  
  @abstractmethod
  def to_json(self): pass