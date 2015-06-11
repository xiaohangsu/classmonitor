var gulp = require('gulp');
var changed = require('gulp-changed');
var run = require('gulp-run');
//Gulp JS Plugins
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
//Gulp CSS Plugins
var cssmin = require('gulp-cssmin');
var concatCss = require('gulp-concat-css');
var csslint = require('gulp-csslint');
//Uglify Options
var uglify_opts = {
	sequences     : true,  // join consecutive statemets with the “comma operator”
	properties    : true,  // optimize property access: a["foo"] → a.foo
	dead_code     : true,  // discard unreachable code
	drop_debugger : true,  // discard “debugger” statements
	unsafe        : false, // some unsafe optimizations (see below)
	conditionals  : true,  // optimize if-s and conditional expressions
	comparisons   : true,  // optimize comparisons
	evaluate      : true,  // evaluate constant expressions
	booleans      : true,  // optimize boolean expressions
	loops         : true,  // optimize loops
	unused        : true,  // drop unused variables/functions
	hoist_funs    : true,  // hoist function declarations
	hoist_vars    : false, // hoist variable declarations
	if_return     : true,  // optimize if-s followed by return/continue
	join_vars     : true,  // join var declarations
	cascade       : true,  // try to cascade `right` into `left` in sequences
	side_effects  : true,  // drop side-effect-free statements
	warnings      : true,  // warn about potentially dangerous optimizations/code
	global_defs   : {}     // global definitions
}

gulp.task('js', function() {
	console.log('[' + (new Date()).toLocaleTimeString() + '] ' + '检查JS语法错误并进行压缩合并...');
	return gulp.src('./static/js/src/*.js')
		//.pipe(changed('./js/src*.js'))
		.pipe(jshint())
    .pipe(jshint.reporter(stylish))
    //.pipe(jshint.reporter('fail'))
		.pipe(uglify(uglify_opts))
		.pipe(concat('build.js'))
		.pipe(gulp.dest('./static/'));
});

gulp.task('css', function() {
	console.log('[' + (new Date()).toLocaleTimeString() + '] ' + '检查CSS语法错误并进行压缩合并...');
	return gulp.src('./static/css/src/*.css')
		//.pipe(changed('./css/src*.css'))
		.pipe(csslint())
		.pipe(csslint.reporter())
		.pipe(cssmin())
		.pipe(concatCss('build.css'))
		.pipe(gulp.dest('./static/'));
});

gulp.task('watch', function() {
	console.log('[' + (new Date()).toLocaleTimeString() + '] ' + '[JS|CSS] 文件改动监测中...');
	gulp.watch('./static/js/src/*.js', ['js']);
	gulp.watch('./static/css/src/*.css', ['css']);
});

gulp.task('server', function() {
	console.log('[' + (new Date()).toLocaleTimeString() + '] ' + '服务器开启...');
	run('python index.py').exec();
});

gulp.task('default', ['js', 'css', 'server', 'watch']);
