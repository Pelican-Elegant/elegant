import fs from "fs";
import path from "path";
import { watch, parallel } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
const browserSync = browserSyncCreate();

const path404 = path.join(__dirname, "documentation/output/404.html");
const content_404 = () =>
  fs.existsSync(path404) ? fs.readFileSync(path404) : null;


const buildAll = () => exec("cd documentation && invoke build");

const reload = cb => {
  browserSync.init(
    {
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
    },
    (_, bs) => {
      bs.addMiddleware("*", (_, res) => {
        res.write(content_404());
        res.end();
      });
    }
  );
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
