import { watch, parallel } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
const browserSync = browserSyncCreate();

const buildAll = () => exec("cd documentation && invoke build");

const reload = cb => {
  browserSync.init({
    ui: {
      port: 9002
    },
    server: {
      baseDir: "documentation/output",
      serveStaticOptions: {
        extensions: ["html"]
      }
    },
    files: "documentation/output/*.html",
    port: 9001
  });
  cb();
};

const watchFiles = () => {
  watch(
    [
      "documentation/content/**/*.md",
      "documentation/content/**/*.rest",
      "documentation/pelicanconf.py",
      "documentation/publishconf.py",
      "templates/**/*.html",
      "static/**/*.css",
      "static/**/*.js"
    ],
    { ignoreInitial: false },
    buildAll
  );
};

const elegant = parallel(watchFiles, reload);

exports.elegant = elegant;
exports.default = elegant;
