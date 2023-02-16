#include <filesystem>
using namespace fs = std::filesystem;

auto get_files(std::string path)
{
    return fs::directory_iterator(path);
}

auto get_procs()
{
    return get_files("/proc");
}

auto get_procs_opendir()
{
    vector<string> proc_ids;
    dirp = opendir("/proc");
    while ((dp = readdir(dirp)) != NULL)
    {
        proc_ids.push_back(dp->d_name);
    }
    return proc_ids;
}

auto get_mac_address(ifname = "eth0")
{
    const fs::path mac_file{"/sys/class/net"} / ifname / "address";
    std::ifstream f(mac_file, std::ios::in);
    const auto size = fs::file_size(mac_file);
    std::string result(size, '\0');
    f.read(result.data(), sz);
    return result;
}

int main(void)
{
    files = get_files(".");
    for (const auto &entry : files)
    {
        cout << entry.path() << endl;
    }
    procs = get_procs();
    for (const auto &entry : procs)
    {
        cout << entry.filename() << endl;
    }
    auto mac_addr = get_mac_address();
    cout << mac_addr << endl;
}
