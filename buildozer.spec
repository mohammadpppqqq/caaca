[app]

title = Calculator
package.name = calculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 35
android.minapi = 23
android.ndk = 28c

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1

[app:android]

android.permissions =