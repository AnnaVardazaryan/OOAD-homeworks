class Multiton:
    instances = []
    limit = 2
    current_index = 0

    def __init__(self):
        Multiton.current_index = (Multiton.current_index + 1) % Multiton.limit

    @classmethod
    def get_instance(cls):
        if len(cls.instances) < cls.limit:
            instance = Multiton()
            cls.instances.append(instance)
        else:
            instance = cls.instances[cls.current_index]
            cls.current_index = (cls.current_index + 1) % cls.limit
        return instance


instance1 = Multiton.get_instance()
instance2 = Multiton.get_instance()
instance3 = Multiton.get_instance()
instance4 = Multiton.get_instance()

print(instance1 is instance2)  # False
print(instance1 is instance3)  # True
print(instance1 is instance4)  # False
print(instance2 is instance3)  # False
print(instance2 is instance4)  # True
print(instance3 is instance4)  # False