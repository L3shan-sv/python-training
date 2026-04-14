import json

class Service:
    def __init__(self, name, status, restart_count=0):
        self.name = name
        self.status = status
        self.restart_count = restart_count

    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status,
            "restart_count": self.restart_count,
        }

    @staticmethod
    def from_dict(data):
        return Service(
            data["name"],
            data["status"],
            data["restart_count"],
        )


class ServiceRegistry:
    def __init__(self, filename="service.json"):
        self.filename = filename
        self.services = []
        self.load()

    def service_add(self, service):
        self.services.append(service)
        self.save()

    def service_list(self):
        return [s.to_dict() for s in self.services]

    def service_get(self, name):
        for s in self.services:
            if s.name == name:
                return s
        return None

    def service_update(self, name, status):
        service = self.service_get(name)
        if service:
            if service.status != "running" and status == "running":
                service.restart_count += 1
            service.status = status
            self.save()
            return True
        return False

    def service_delete(self, name):
        service = self.service_get(name)
        if service:
            self.services.remove(service)
            self.save()
            return True
        return False

    # 💾 Persistence
    def save(self):
        data = [s.to_dict() for s in self.services]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.services = [Service.from_dict(d) for d in data]
        except FileNotFoundError:
            self.services = []