#include <demo/demo.hpp>
#include <iostream>
#include <sstream>
#include <stdexcept>

std::uint64_t parse_number(const char* arg)
{
    std::stringstream stream(arg);
    
    std::uint64_t result = 0;
    stream >> result;

    if (stream.fail())
    {
        throw std::runtime_error("Failed to parse the input.");
    }

    return result;
}

int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        std::cout << "This application calculates the gauss sum. Please specify n as first argument.\n";
        return -1;
    }

    try
    {
        const auto n = parse_number(argv[1]);
        const auto result = demo::gauss(n);
        std::cout << result << "\n";
    }
    catch(const std::exception& ex)
    {
        std::cerr << ex.what() << "\n";
        return -1;
    }

    return 0;
}
