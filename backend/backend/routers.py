import sys


class TestDbRouter:
    def db_for_read(self, model, **hints):
        if 'test' in sys.argv:
            return 'test'
        return None

    def db_for_write(self, model, **hints):
        if 'test' in sys.argv:
            return 'test'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
