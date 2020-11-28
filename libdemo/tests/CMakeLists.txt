find_package(GTest REQUIRED)

set(DEMO_TEST_SOURCES   "${CMAKE_CURRENT_SOURCE_DIR}/demo_tests.cpp"
                        "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp")

add_executable(demo_tests ${DEMO_TEST_SOURCES})
target_link_libraries(demo_tests PUBLIC demo GTest::GTest)

