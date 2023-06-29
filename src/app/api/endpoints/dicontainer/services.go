package dicontainer

import (
	"keihi-kanri/src/core/errors/logger"
	"keihi-kanri/src/core/interfaces/primary"
	"keihi-kanri/src/core/services"
)

func GetUserServices() primary.UserManager {
	return services.NewUserServices(GetUserRepository(), GetLogger())
}

func GetLogger() logger.Logger {
	return logger.New()
}
