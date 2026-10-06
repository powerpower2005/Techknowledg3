---
title: Linux 파일 시스템
category: operating-systems
tags:
- filesystem
- linux
- operating-systems
- storage
status: note
visibility: public
publication_reviewed_at: '2026-10-06'
---

# 파일 시스템

프로세스 - 파일 시스템 코드(커널) - 하드웨어(저장 장치)


## 파일시스템

- 데이터
사용자가 작성한 문서, 영상, 동영상, 프로그램 등

- 메타 데이터
파일 관리 목적으로 갖고 있는 데이터(파일 종류, 파일 시각 정보, 파일 권한 정보, 디렉터리 데이터)


## 파일 접근 방법
POSIX에서 지정한 함수로 접근 가능



# mmap - memory mapping
메모리 맵 파일 기능
mmap() 함수를 특정한 방법으로 호출하면
파일을 프로세스의 가상 주소 공간에 매핑한다. 필요한 페이지는 실제 접근 시 읽힐 수 있다. 변경의 공유·파일 반영 여부는 MAP_SHARED 또는 MAP_PRIVATE와 보호 옵션 등을 확인한다.


1.  /proc/<pid>/maps 를 통해 프로세스 메모리 맵 파악
2. 파일을 mmap() 이용해서 메모리 공간에 매핑
3. 프로세스 메모리 맵 상황 재 출력
4. 매핑된 영역의 데이터를 변경



# 일반적인 파일 시스템
- ext4
- XFS
- Btrfs


# 기타 파일 시스템

## 메모리 기반의 파일 시스템
tmpfs
휘발성 메모리로 사용

/tmp, /var/run 들에서 사용하곤 함


## 네트워크 파일 시스템
네트워크로 연결된 원격 호스트의 데이터에 파일 시스템 인터페이스를 사용해서 접근
NFS

여러 기기의 저장장치를 하나로 묶어서 커다란 하나의 파일 시스템으로 만드는 CephFS 같은 파일 시스템도 존재함



## procfs
..
## sysfs
..





-------------------

# 참고 링크

[Understanding File System Superblock in Linux](https://www.slashroot.in/understanding-file-system-superblock-linux)

[Overview of the Linux Virtual File System](https://www.kernel.org/doc/html/latest/filesystems/vfs.html)

[LinuxVFS (COMSW4118 lecture, Kaustubh R. Joshi)](http://www.cs.columbia.edu/~krj/os/lectures/L21-LinuxVFS.pdf)

[Filesystems in the Linux kernel — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/)

[A Linux user's guide to Logical Volume Management](https://opensource.com/business/16/9/linux-users-guide-lvm)

[Linux LVM Cheat Sheet](https://unixutils.com/lvm-cheat-sheet-quick-reference/)

[fstab - ArchWiki](https://wiki.archlinux.org/title/Fstab)

[Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

[Using the /dev and /proc file systems - Linux.com](https://www.linux.com/news/using-dev-and-proc-file-systems/)

[The /proc Filesystem — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html)

[Tmpfs — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/tmpfs.html)

[DebugFS — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/debugfs.html)

[LKML: Christian Brauner on loopfs](https://lkml.org/lkml/2020/4/8/506)

[The SWAPFS file system](https://linux.die.net/EVMSUG/x3863.html)

[Linux NTFS Project](https://flatcap.org/linux-ntfs/misc.html)

[OpenZFS Documentation — OpenZFS documentation](https://openzfs.github.io/openzfs-docs/)

[Filesystems Benchmarked » Linux Magazine](https://www.linux-magazine.com/Online/Features/Filesystems-Benchmarked)

[Overlay Filesystem — The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html)

[btrfs Wiki](https://btrfs.wiki.kernel.org/index.php/Main_Page)

[Unionfs: A Stackable Unification File System](https://unionfs.filesystems.org/)

[Kernel Korner - Unionfs: Bringing Filesystems Together](https://www.linuxjournal.com/article/7714)

[Unifying filesystems with union mounts - LWN.net](https://lwn.net/Articles/312641/)

[Persistent BPF objects - LWN.net](https://lwn.net/Articles/664688/)

<!-- BEGIN WIKI NAV -->

---

상태: **노트** · 태그: [#filesystem](../../tags.md#filesystem) · [#linux](../../tags.md#linux) · [#operating-systems](../../tags.md#operating-systems) · [#storage](../../tags.md#storage)

[주제 목차](../index.md) · [위키 홈](../../index.md)

<!-- END WIKI NAV -->
