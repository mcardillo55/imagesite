#!/usr/bin/env bash
#
# Build a Lambda deployment zip for the imgsite Django app.
#
# Usage:  ./build.sh
# Output: imgsite-lambda.zip in the current directory.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$SCRIPT_DIR/.build"
ZIP_NAME="imgsite-lambda.zip"

echo "==> Cleaning previous build..."
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "==> Installing Python dependencies..."
pip install \
    --quiet \
    --target "$BUILD_DIR" \
    -r "$SCRIPT_DIR/requirements.txt"

echo "==> Copying application code..."
# Copy the Django project files (not the build artifacts or venvs)
cp "$SCRIPT_DIR/lambda_handler.py" "$BUILD_DIR/"
cp "$SCRIPT_DIR/manage.py"         "$BUILD_DIR/"
cp "$SCRIPT_DIR/db.sqlite3"        "$BUILD_DIR/"
cp -r "$SCRIPT_DIR/imagesite"      "$BUILD_DIR/imagesite"
cp -r "$SCRIPT_DIR/images"         "$BUILD_DIR/images"
cp -r "$SCRIPT_DIR/static"         "$BUILD_DIR/static"

echo "==> Creating deployment zip..."
cd "$BUILD_DIR"
zip -qr "$SCRIPT_DIR/$ZIP_NAME" .

echo "==> Done!  $ZIP_NAME is $(du -h "$SCRIPT_DIR/$ZIP_NAME" | cut -f1)"
echo ""
echo "Lambda configuration:"
echo "  Handler:  lambda_handler.handler"
echo "  Runtime:  python3.12"
echo "  Env vars:"
echo "    DJANGO_SETTINGS_MODULE=imagesite.settings"
echo "    IMAGE_BASE_URL=https://<your-cloudfront-dist>.cloudfront.net/imgsite/img"
echo "    ALLOWED_HOSTS=<your-domain>"
