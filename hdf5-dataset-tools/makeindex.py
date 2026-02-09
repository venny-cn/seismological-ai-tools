import os
import argparse
import stat

def make_h5(args):
    # 确保 mseedidx 有执行权限
    mseedidx_path = os.path.join(os.path.dirname(__file__), "utils", "mseedidx")
    add_execute_permission(mseedidx_path)

    os.environ['LIBMSEED_LEAPSECOND_FILE'] = "utils/leap-seconds.list"
    count = 0
    for root, dirs, files in os.walk(args.root):
        for f in files:
            if f.endswith(".mseed"):
                path = os.path.join(root, f)
                os.system(f"utils/mseedidx -sqlite {args.out} {path}")
                count += 1
                if count % 100 == 0:
                    print("已完成", count, path)


def add_execute_permission(filepath):
    """为文件添加执行权限"""
    if os.path.exists(filepath):
        current_permissions = os.stat(filepath).st_mode
        os.chmod(filepath, current_permissions | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        print(f"已为 {filepath} 添加执行权限")
    else:
        print(f"文件 {filepath} 不存在")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='制作索引')
    parser.add_argument("-r", "--root", type=str, help="搜索路径")
    parser.add_argument("-o", "--out", type=str, help="文件位置")
    args = parser.parse_args()
    args.root = "/Volumes/extends/data/download"
    args.out = "data/index.sqlite"
    # 验证输入路径存在
    if not os.path.exists(args.root):
        print(f"错误: 输入路径 {args.root} 不存在")
        exit(1)

    # 验证输出路径的目录存在
    output_dir = os.path.dirname(args.out)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"创建输出目录: {output_dir}")
        except Exception as e:
            print(f"错误: 无法创建输出目录 {output_dir}: {e}")
            exit(1)

    print(f"开始处理路径: {args.root}")
    print(f"输出文件: {args.out}")

    try:
        make_h5(args)
        print("索引制作完成!")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")
        exit(1)
