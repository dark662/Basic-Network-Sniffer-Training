Network Sniffer مكتشف الشبكة
Overview ملخص

This project is a network sniffer tool implemented in Python. It captures and analyzes network traffic, providing detailed information about each packet. The tool utilizes the Npcap library for packet capture on Windows systems.
هذا المشروع عبارة عن أداة تحسس شبكة يتم تنفيذها في بايثون. فهو يلتقط ويحلل حركة مرور الشبكة، ويوفر معلومات مفصلة حول كل حزمة. تستخدم الأداة مكتبة Npcap لالتقاط الحزم على أنظمة Windows.
Features سمات

    Captures network packets in real-time.
    يلتقط حزم الشبكة في الوقت الحقيقي.
    Provides detailed information about each packet, including source and destination IP addresses, protocol, packet length, time of capture, TTL, flags, and more.
    يوفر معلومات مفصلة حول كل حزمة، بما في ذلك عناوين IP المصدر والوجهة، والبروتوكول، وطول الحزمة، ووقت الالتقاط، وTTL، والأعلام، والمزيد.
    Supports analysis of various protocols such as TCP, UDP, and ICMP.
    يدعم تحليل البروتوكولات المختلفة مثل TCP، UDP، وICMP.
    Displays source and destination MAC addresses for Ethernet packets.
    يعرض عناوين MAC المصدر والوجهة لحزم Ethernet.
    Supports capturing and analyzing fragmented IP packets.
    يدعم التقاط وتحليل حزم IP المجزأة.
    Provides TCP-specific information such as sequence numbers, acknowledgment numbers, and TCP flags.
    يوفر معلومات خاصة بـ TCP مثل أرقام التسلسل وأرقام الإقرار وإشارات TCP.

Installation تثبيت
Install the required dependencies:
تثبيت التبعيات المطلوبة:

    pip install scapy نقطة تثبيت scapy
