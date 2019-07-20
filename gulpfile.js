const { watch, parallel } = require("gulp");
const { exec } = require("child_process");
const browserSync = require("browser-sync").create();

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
    ["documentation/content/**/*.md", "documentation/content/**/*.rest"],
    { ignoreInitial: false },
    buildAll
  );
};

const elegant = parallel(watchFiles, reload);

exports.elegant = elegant;
exports.default = elegant;
