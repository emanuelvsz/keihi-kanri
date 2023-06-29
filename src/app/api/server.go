package main

import (
	"fmt"
	"keihi-kanri/src/app/api/endpoints/routes"
	"keihi-kanri/src/app/api/middlewares"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func serve(host string, port int) {
	router := echo.New()
	router.Use(middleware.Logger())
	router.Use(middleware.Recover())
	router.Use(getCORSSettings())

	apiGroup := router.Group("/api")

	rout := routes.New()
	rout.Load(apiGroup)

	address := getServerAddress(host, port)
	router.Logger.Fatal(router.Start(address))
}

func getServerAddress(host string, port int) string {
	return fmt.Sprintf("%v:%v", host, port)
}

func getCORSSettings() echo.MiddlewareFunc {
	return middleware.CORSWithConfig(middleware.CORSConfig{
		Skipper:         middlewares.OriginInspectSkipper,
		AllowOriginFunc: middlewares.VerifyOrigin,
		AllowMethods: []string{
			http.MethodHead,
			http.MethodGet,
			http.MethodPost,
			http.MethodPut,
			http.MethodDelete,
			http.MethodPatch,
		},
	})
}