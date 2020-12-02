#include <demo/demo.hpp>
#include <gtest/gtest.h>

class DemoTestFixture : public ::testing::Test
{
};

TEST_F(DemoTestFixture, Gauss_From1To10_Returns55)
{
    const std::uint64_t n = 10;
    const std::uint64_t expected_result = 55;

    const auto result = demo::gauss(n);

    ASSERT_EQ(expected_result, result);
}

TEST_F(DemoTestFixture, Gauss_ZeroInput_ReturnsZero)
{
    const std::uint64_t n = 0;
    const std::uint64_t expected_result = 0;

    const auto result = demo::gauss(n);

    ASSERT_EQ(expected_result, result);
}

