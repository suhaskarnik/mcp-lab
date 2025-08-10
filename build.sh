#!/bin/bash

docker compose -f compose/compose.yml \
	--profile stage0 \
	--env-file "$HOME/.env" \
	up -d --build
