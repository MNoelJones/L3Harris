#include <filesystem>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <cctype>

namespace fs = std::filesystem;
using namespace std;

auto get_files(std::string path)
{
    return fs::directory_iterator(path);
}

bool is_number(const std::string& s) {
    return !s.empty() && std::find_if(
        s.begin(), s.end(),
        [](unsigned char c) { return !std::isdigit(c); }
    ) == s.end();
}

auto get_procs()
{
    vector<string> proc_ids;
    for (const auto & entry : get_files("/proc")) {
        if (entry.is_directory()) {

            if (is_number(entry.path().filename().string())) {
                proc_ids.push_back(entry.path().filename().string());
            }
        }
    }
    return proc_ids;
}

// auto get_procs_opendir()
// {
//     vector<string> proc_ids;
//     auto dirp = opendir("/proc");
//     while ((dp = readdir(dirp)) != NULL)
//     {
//         proc_ids.push_back(dp->d_name);
//     }
//     return proc_ids;
// }

auto get_mac_address(std::string ifname="eth0")
{
    const fs::path mac_file_pre{"/sys/class/net"};
    fs::path mac_file = mac_file_pre / ifname / "address";
    std::ifstream f(mac_file, std::ios::in);
    const auto size = fs::file_size(mac_file);
    std::string result(size, '\0');
    f.read(result.data(), size);
    return result;
}

int main(void)
{
    auto files = get_files(".");
    for (const auto &entry : files)
    {
        cout << entry.path() << endl;
    }
    auto procs = get_procs();
    for (const auto &entry : procs)
    {
        cout << entry << endl;
    }
    auto mac_addr = get_mac_address("enp0s3");
    cout << mac_addr << endl;
}
