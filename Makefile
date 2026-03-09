SHELL := /bin/bash
export SHELLOPTS := errexit:pipefail

.DEFAULT: dryrun

dryrun: dryrun = 1
dryrun: publish

publish:
	rsync -av --no-owner --no-group --delete --itemize-changes $(if $(dryrun),--dry-run,) \
		--chmod=u=rwX,og=rX \
		--exclude='.git*' \
		. tsibley.net:www/seattle/biketag/
