#include "demo/demo.hpp"

std::uint64_t demo::gauss(const std::uint64_t n)
{
    return (n * n + n) >> 1;
}

