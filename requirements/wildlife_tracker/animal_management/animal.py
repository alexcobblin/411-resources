from typing import Any, Optional

class Animal:
    age: Optional[int] = None
    animal_id: int
    health_status: Optional[str] = None
    species: str
    def get_animal_details(animal_id) -> dict[str, Any]:
        pass
    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass


    pass
