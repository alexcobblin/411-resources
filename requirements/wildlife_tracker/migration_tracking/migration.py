from typing import Any

class Migration:
    migration_id: int
    species: str
    def get_migration_by_id(migration_id: int) -> Migration:
        pass
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
        
    pass