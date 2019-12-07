import fs from "fs";
import path from "path";
import { src, dest, watch, parallel, series } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
import postcss from "gulp-postcss";
import cssnano from "cssnano";
import postcssPresetEnv from "postcss-preset-env";
import concat from "gulp-concat";

const browserSync = browserSyncCreate();

const path404 = path.join(__dirname, "documentation/output/404.html");
const content_404 = () =>
  fs.existsSync(path404) ? fs.readFileSync(path404) : null;

const cleanOutput = () => exec("cd documentation && rm -rf outout/");

const buildContent = () => exec("cd documentation && invoke build");

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
      "!static/**/elegant.prod.css",
      "static/**/*.js"
    ],
    { ignoreInitial: false },
    buildAll
  );
};

const pathProdCSS = path.join(__dirname, "static/css/elegant.prod.css");
const rmProdCSS = cb => {
  if (fs.existsSync(pathProdCSS)) {
    fs.unlinkSync(pathProdCSS);
  }
  cb();
};

const compileCSS = () => {
  const plugins = [
    // postcssPresetEnv comes with autoprefixer
    postcssPresetEnv({ stage: 1 }),
    cssnano()
  ];
  return src([
    "static/applause-button/applause-button.css",
    "static/tipuesearch/tipuesearch.css",
    "static/css/*.css",
    "!static/css/elegant.prod.css"
  ])
    .pipe(postcss(plugins))
    .pipe(concat("elegant.prod.css"))
    .pipe(dest("static/css/"));
};

const buildAll = series(rmProdCSS, compileCSS, buildContent);
const elegant = series(
  compileCSS,
  cleanOutput,
  buildContent,
  parallel(watchFiles, reload)
);

exports.css = series(rmProdCSS, compileCSS);
exports.elegant = elegant;
exports.default = elegant;
