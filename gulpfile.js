var gulp = require('gulp'),
	uglify = require('gulp-uglify'),
	minifyCSS = require('gulp-minify-css'),
	concat = require('gulp-concat');
 

gulp.task('styles',function(){
	gulp.src('feribotlines/static/*.css')
		.pipe(minifyCSS({keepBreaks : true}))
		.pipe(concat('app.min.css'))
		.pipe(gulp.dest('feribotlines/static/dist/css'))
});
 
 
gulp.task('watch',function(){	
    gulp.watch('app/css/*.css',['styles']);
});
gulp.task('default', [ 'styles','watch']);