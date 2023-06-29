package dicontainer

import "keihi-kanri/src/app/api/endpoints/handlers"

func GetUserHandlers() *handlers.UserHandlers {
	return handlers.NewUserHandlers(GetUserServices())
}
