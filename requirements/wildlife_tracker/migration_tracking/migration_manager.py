from typing import Optional
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:
    migration_path: MigrationPath
    paths: dict[int, MigrationPath] = {}

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass
    def schedule_migration(migration_path: MigrationPath) -> None:
        pass
    def get_migration_paths() -> list[MigrationPath]:
        pass
    

    pass
