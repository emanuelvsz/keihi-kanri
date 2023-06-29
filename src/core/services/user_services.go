package services

import (
	"keihi-kanri/src/core/errors/logger"
	"keihi-kanri/src/core/interfaces/primary"
	"keihi-kanri/src/core/interfaces/repository"
)

var _ primary.UserManager = (*UserServices)(nil)

type UserServices struct {
	userRepository repository.UserLoader
	logger         logger.Logger
}

func NewUserServices(userRepository repository.UserLoader, logger logger.Logger) *UserServices {
	return &UserServices{
		userRepository: userRepository,
		logger:         logger,
	}
}
