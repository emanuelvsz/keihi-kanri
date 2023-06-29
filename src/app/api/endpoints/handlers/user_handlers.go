package handlers

import (
	"keihi-kanri/src/core/interfaces/primary"
)

type UserHandlers struct {
	service primary.UserManager
}

func NewUserHandlers(service primary.UserManager) *UserHandlers {
	return &UserHandlers{service: service}
}
