[app]
title = Discount App
package.name = discountapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,gtts,requests,urllib3,chardet,idna
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
