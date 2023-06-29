package dicontainer

import (
	"keihi-kanri/src/core/interfaces/repository"
	"keihi-kanri/src/infra/postgres"
)

func GetUserRepository() repository.UserLoader {
	return postgres.NewUserPostgresRepository(GetPsqlConnectionManager())
}

func GetPsqlConnectionManager() *postgres.DatabaseConnectionManager {
	return &postgres.DatabaseConnectionManager{}
}
