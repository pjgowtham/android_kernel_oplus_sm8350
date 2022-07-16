ifeq ($(CONFIG_OPPO_FINGERPRINT_MTK),y)
obj-y += jiiov_platform_mtk.o jiiov_netlink.o
else
obj-$(CONFIG_OPPO_FINGERPRINT_JIIOV_OPTICAL) += jiiov_qcom.o
jiiov_qcom-y := jiiov_platform.o jiiov_netlink.o
endif
