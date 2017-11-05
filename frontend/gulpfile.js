const gulp = require("gulp");
const sass = require("gulp-sass");
const stylus = require("gulp-stylus");
const autoprefixer = require("gulp-autoprefixer");
const minify_css = require("gulp-minify-css");
const sourcemaps = require("gulp-sourcemaps");
const uglify = require("gulp-uglify");
const babel = require("gulp-babel");
const include = require("gulp-include");
const path = require("path");

gulp.task("babel", function() {
  gulp
    .src("./assets/js/**/*.js")
    .pipe(include())
    .pipe(sourcemaps.init())
    .pipe(
      babel({
        presets: ["env"]
      })
    )
    .pipe(uglify())
    .pipe(sourcemaps.write("."))
    .pipe(gulp.dest("./dist/js/"));
});

gulp.task("scss", function() {
  gulp
    .src("./assets/scss/**/*.scss")
    .pipe(sourcemaps.init())
    .pipe(
      sass(
        {
          // includePaths: []
          // imagePath: "path/to/images"
        }
      ).on("error", sass.logError)
    )
    .pipe(
      autoprefixer("last 2 version", "> 1%", "Explorer >= 8", {
        cascade: true
      })
    )
    .pipe(minify_css({ compatibility: "ie8" }))
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest("./dist/css/"));
});

gulp.task("stylus", function() {
  gulp
    .src("./assets/styl/**/*.styl")
    .pipe(sourcemaps.init())
    .pipe(
      stylus(
        {
          compress: true
        }
      )
    )
    .pipe(
      autoprefixer("last 2 version", "> 1%", "Explorer >= 8", {
        cascade: true
      })
    )
    .pipe(minify_css({ compatibility: "ie8" }))
    .pipe(sourcemaps.write("./"))
    .pipe(gulp.dest("./dist/css/"));
});

gulp.task("fonts", function() {
  gulp.src("./assets/fonts/**/*").pipe(gulp.dest("./dist/fonts"));
});

gulp.task("images", function() {
  gulp.src("./assets/images/**/*").pipe(gulp.dest("./dist/images"));
});

gulp.task("watcher", function() {
  gulp.watch("./assets/scss/**/*.scss", ["scss"]);
  gulp.watch("./assets/styl/**/*.styl", ["stylus"]);
  gulp.watch("./assets/js/**/*.js", ["babel"]);
});

gulp.task("default", ["scss", "stylus", "babel", "fonts", "images", "watcher"]);
