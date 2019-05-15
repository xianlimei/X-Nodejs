{

  'targets': [
    {
      'target_name': 'spdlog',
      'type': '<(library)',
      'include_dirs': [
        'include'
      ],
      'cflags': ['-fexceptions','-Wall','-O3'],
      'compflags':['-fexceptions'],
      'cflags_cc': ['-fexceptions','-Wall','-O3'],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'defines':[

      ],
      'direct_dependent_settings': {
              'include_dirs': [ 'include' ]
      },

      'conditions': [
        ['OS in "freebsd dragonflybsd linux openbsd solaris android aix"', {

       'cflags!': ['-fno-exceptions'],
       'cflags_cc!': ['-fno-exceptions']
        }]
      ],

      'sources': [
'include/spdlog/async.h',
'include/spdlog/async_logger.h',
'include/spdlog/common.h',
'include/spdlog/details/async_logger_impl.h',
'include/spdlog/details/circular_q.h',
'include/spdlog/details/console_globals.h',
'include/spdlog/details/file_helper.h',
'include/spdlog/details/fmt_helper.h',
'include/spdlog/details/logger_impl.h',
'include/spdlog/details/log_msg.h',
'include/spdlog/details/mpmc_blocking_q.h',
'include/spdlog/details/null_mutex.h',
'include/spdlog/details/os.h',
'include/spdlog/details/pattern_formatter.h',
'include/spdlog/details/periodic_worker.h',
'include/spdlog/details/registry.h',
'include/spdlog/details/thread_pool.h',
'include/spdlog/fmt/bin_to_hex.h',
'include/spdlog/fmt/bundled/chrono.h',
'include/spdlog/fmt/bundled/color.h',
'include/spdlog/fmt/bundled/core.h',
'include/spdlog/fmt/bundled/format.h',
'include/spdlog/fmt/bundled/format-inl.h',
'include/spdlog/fmt/bundled/LICENSE.rst',
'include/spdlog/fmt/bundled/locale.h',
'include/spdlog/fmt/bundled/ostream.h',
'include/spdlog/fmt/bundled/posix.h',
'include/spdlog/fmt/bundled/printf.h',
'include/spdlog/fmt/bundled/ranges.h',
'include/spdlog/fmt/bundled/time.h',
'include/spdlog/fmt/fmt.h',
'include/spdlog/fmt/ostr.h',
'include/spdlog/formatter.h',
'include/spdlog/logger.h',
'include/spdlog/sinks/android_sink.h',
'include/spdlog/sinks/ansicolor_sink.h',
'include/spdlog/sinks/base_sink.h',
'include/spdlog/sinks/basic_file_sink.h',
'include/spdlog/sinks/daily_file_sink.h',
'include/spdlog/sinks/dist_sink.h',
'include/spdlog/sinks/msvc_sink.h',
'include/spdlog/sinks/null_sink.h',
'include/spdlog/sinks/ostream_sink.h',
'include/spdlog/sinks/rotating_file_sink.h',
'include/spdlog/sinks/sink.h',
'include/spdlog/sinks/stdout_color_sinks.h',
'include/spdlog/sinks/stdout_sinks.h',
'include/spdlog/sinks/syslog_sink.h',
'include/spdlog/sinks/systemd_sink.h',
'include/spdlog/sinks/wincolor_sink.h',
'include/spdlog/spdlog.h',
'include/spdlog/tweakme.h',
'include/spdlog/version.h'

      ]
    }
  ]
}