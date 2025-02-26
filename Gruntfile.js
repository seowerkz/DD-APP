module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
        app_less: {
            files: ['doubleddistributionapp/static/admin/less/*', '!doubleddistributionapp/static/admin/less/variables.less'],
            tasks: ['less:app_less', 'cssmin:app_css']
        },
        drivers: {
            files: ['drivers/static/drivers/js/source/*'],
            tasks: ['drivers']
        },
        drivers_less: {
            files: ['drivers/static/drivers/less/*'],
            tasks: ['drivers_less']
        },
        messaging: {
            files: ['messaging/static/messaging/js/source/*'],
            tasks: ['messaging']
        },
        messaging_less: {
            files: ['messaging/static/messaging/less/*'],
            tasks: ['messaging_less']
        },
        office: {
            files: ['office/static/office/js/source/*'],
            tasks: ['office']
        },
        office_less: {
            files: ['office/static/office/less/*'],
            tasks: ['office_less']
        },
        reminders: {
            files: ['reminders/static/reminders/js/source/*'],
            tasks: ['reminders']
        },
        reminders_less: {
            files: ['reminders/static/reminders/less/*'],
            tasks: ['reminders_less']
        },
        shop: {
            files: ['shop/static/shop/js/source/*'],
            tasks: ['shop']
        },
        shop_less: {
            files: ['shop/static/shop/less/*'],
            tasks: ['shop_less']
        }
    },
    less: {
        app_less: {
            files: [
                {
                    expand: true,
                    cwd: 'doubleddistributionapp/static/admin/less',
                    src: ['**/*.less', '!variables.less'],
                    dest: 'doubleddistributionapp/static/admin/css',
                    ext: '.css',
                    compress: true
                }
            ]
        },
        drivers_less: {
            files: [
                {
                    expand: true,
                    cwd: 'drivers/static/drivers/less',
                    src: '**/*.less',
                    dest: 'drivers/static/drivers/css',
                    ext: '.css',
                    compress: true
                }
            ]
        },
        messaging_less: {
            files: [
                {
                    expand: true,
                    cwd: 'messaging/static/messaging/less',
                    src: '**/*.less',
                    dest: 'messaging/static/messaging/css',
                    ext: '.css',
                    compress: true
                }
            ]
        },
        office_less: {
            files: [
                {
                    expand: true,
                    cwd: 'office/static/office/less',
                    src: '**/*.less',
                    dest: 'office/static/office/css',
                    ext: '.css',
                    compress: true
                }
            ]
        },
        reminders_less: {
            files: [
                {
                    expand: true,
                    cwd: 'reminders/static/reminders/less',
                    src: '**/*.less',
                    dest: 'reminders/static/reminders/css',
                    ext: '.css',
                    compress: true
                }
            ]
        },
        shop_less: {
            files: [
                {
                    expand: true,
                    cwd: 'shop/static/shop/less',
                    src: '**/*.less',
                    dest: 'shop/static/shop/css',
                    ext: '.css',
                    compress: true
                }
            ]
        }
    },
    cssmin: {
        app_css: {
            files: [{
                expand: true,
                cwd: 'doubleddistributionapp/static/admin/css',
                src: '**/*.css',
                dest: 'doubleddistributionapp/static/admin/css',
                ext: '.css'
            }]
        },
        drivers_css: {
            files: [
                {
                    expand: true,
                    cwd: 'drivers/static/drivers/css',
                    src: '**/*.css',
                    dest: 'drivers/static/drivers/css',
                    ext: '.css'
                }
            ]
        },
        messaging_css: {
            files: [
                {
                    expand: true,
                    cwd: 'messaging/static/messaging/css',
                    src: '**/*.css',
                    dest: 'messaging/static/messaging/css',
                    ext: '.css'
                }
            ]
        },
        office_css: {
            files: [
                {
                    expand: true,
                    cwd: 'office/static/office/css',
                    src: '**/*.css',
                    dest: 'office/static/office/css',
                    ext: '.css'
                }
            ]
        },
        reminders_css: {
            files: [
                {
                    expand: true,
                    cwd: 'reminders/static/reminders/css',
                    src: '**/*.css',
                    dest: 'reminders/static/reminders/css',
                    ext: '.css'
                }
            ]
        },
        shop_css: {
            files: [
                {
                    expand: true,
                    cwd: 'shop/static/shop/css',
                    src: '**/*.css',
                    dest: 'shop/static/shop/css',
                    ext: '.css'
                }
            ]
        }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> */\n'
      },
      drivers: {
        files: [
            {
                expand: true,
                cwd: 'drivers/static/drivers/js/source',
                src: '**/*.js',
                dest: 'drivers/static/drivers/js',
                ext: '.min.js'
            }
        ]
      },
      messaging: {
        files: [
            {
                expand: true,
                cwd: 'messaging/static/messaging/js/source',
                src: '**/*.js',
                dest: 'messaging/static/messaging/js',
                ext: '.min.js'
            }
        ]
      },
      office: {
        files: [
            {
                expand: true,
                cwd: 'office/static/office/js/source',
                src: '**/*.js',
                dest: 'office/static/office/js',
                ext: '.min.js'
            }
        ]
      },
      reminders: {
        files: [
            {
                expand: true,
                cwd: 'reminders/static/reminders/js/source',
                src: '**/*.js',
                dest: 'reminders/static/reminders/js',
                ext: '.min.js'
            }
        ]
      },
      shop: {
        files: [
            {
                expand: true,
                cwd: 'shop/static/shop/js/source',
                src: '**/*.js',
                dest: 'shop/static/shop/js',
                ext: '.min.js'
            }
        ]
      }
    }
  });

  // Plugins
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['uglify', 'less', 'cssmin']);
  // Uglify Tasks
  grunt.registerTask('drivers', ['uglify:drivers']);
  grunt.registerTask('messaging', ['uglify:messaging']);
  grunt.registerTask('office', ['uglify:office']);
  grunt.registerTask('reminders', ['uglify:reminders']);
  grunt.registerTask('shop', ['uglify:shop']);
  // LESS Tasks
  grunt.registerTask('app_less', ['less:app_less']);
  grunt.registerTask('drivers_less', ['less:drivers_less']);
  grunt.registerTask('messaging_less', ['less:messaging_less']);
  grunt.registerTask('office_less', ['less:office_less']);
  grunt.registerTask('reminders_less', ['less:reminders_less']);
  grunt.registerTask('shop_less', ['less:shop_less']);
};
