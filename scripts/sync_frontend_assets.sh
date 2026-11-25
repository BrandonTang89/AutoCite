#!/bin/sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
vendor="$root/frontend/vendor"
fomantic="$vendor/fomantic-ui-2.9.4/dist"
web_static="$root/AutoCite_Web/static"
web_dist="$web_static/semantic/semantic/dist"
lambda_static="$root/AutoCite_lambda/static_files"

mkdir -p "$web_dist/themes/default/assets/fonts" "$lambda_static/themes/default/assets/fonts"

cp "$vendor/jquery-4.1.0.min.js" "$web_static/jquery-4.1.0.min.js"
cp "$vendor/jquery-4.1.0.min.js" "$lambda_static/jquery-4.1.0.min.js"
cp "$root/frontend/jquery-4-compat.js" "$web_static/jquery-4-compat.js"
cp "$root/frontend/jquery-4-compat.js" "$lambda_static/jquery-4-compat.js"

cp "$fomantic/semantic.min.js" "$web_dist/semantic.min.js"
cp "$fomantic/semantic.min.css" "$web_dist/semantic.min.css"
cp "$fomantic/semantic.min.js" "$lambda_static/semantic.min.js"
cp "$fomantic/semantic.min.css" "$lambda_static/semantic.min.css"
cp -R "$fomantic/themes/default/assets/fonts/." "$web_dist/themes/default/assets/fonts/"
cp -R "$fomantic/themes/default/assets/fonts/." "$lambda_static/themes/default/assets/fonts/"
