#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method for making a sound."""
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
