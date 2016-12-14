'''
This module contains useful mapping or constants
'''
import vulkan as vk  # pylint: disable=import-error


# Wow! That was long to do!
# The format in bits (not Byte!)
# TODO: Compressed format are not set, not sure of the value
VK_FORMAT_SIZE = {
    vk.VK_FORMAT_UNDEFINED: 0,
    vk.VK_FORMAT_R4G4_UNORM_PACK8: 8,
    vk.VK_FORMAT_R4G4B4A4_UNORM_PACK16: 16,
    vk.VK_FORMAT_B4G4R4A4_UNORM_PACK16: 16,
    vk.VK_FORMAT_R5G6B5_UNORM_PACK16: 16,
    vk.VK_FORMAT_B5G6R5_UNORM_PACK16: 16,
    vk.VK_FORMAT_R5G5B5A1_UNORM_PACK16: 16,
    vk.VK_FORMAT_B5G5R5A1_UNORM_PACK16: 16,
    vk.VK_FORMAT_A1R5G5B5_UNORM_PACK16: 16,
    vk.VK_FORMAT_R8_UNORM: 8,
    vk.VK_FORMAT_R8_SNORM: 8,
    vk.VK_FORMAT_R8_USCALED: 8,
    vk.VK_FORMAT_R8_SSCALED: 8,
    vk.VK_FORMAT_R8_UINT: 8,
    vk.VK_FORMAT_R8_SINT: 8,
    vk.VK_FORMAT_R8_SRGB: 8,
    vk.VK_FORMAT_R8G8_UNORM: 16,
    vk.VK_FORMAT_R8G8_SNORM: 16,
    vk.VK_FORMAT_R8G8_USCALED: 16,
    vk.VK_FORMAT_R8G8_SSCALED: 16,
    vk.VK_FORMAT_R8G8_UINT: 16,
    vk.VK_FORMAT_R8G8_SINT: 16,
    vk.VK_FORMAT_R8G8_SRGB: 16,
    vk.VK_FORMAT_R8G8B8_UNORM: 24,
    vk.VK_FORMAT_R8G8B8_SNORM: 24,
    vk.VK_FORMAT_R8G8B8_USCALED: 24,
    vk.VK_FORMAT_R8G8B8_SSCALED: 24,
    vk.VK_FORMAT_R8G8B8_UINT: 24,
    vk.VK_FORMAT_R8G8B8_SINT: 24,
    vk.VK_FORMAT_R8G8B8_SRGB: 24,
    vk.VK_FORMAT_B8G8R8_UNORM: 24,
    vk.VK_FORMAT_B8G8R8_SNORM: 24,
    vk.VK_FORMAT_B8G8R8_USCALED: 24,
    vk.VK_FORMAT_B8G8R8_SSCALED: 24,
    vk.VK_FORMAT_B8G8R8_UINT: 24,
    vk.VK_FORMAT_B8G8R8_SINT: 24,
    vk.VK_FORMAT_B8G8R8_SRGB: 24,
    vk.VK_FORMAT_R8G8B8A8_UNORM: 32,
    vk.VK_FORMAT_R8G8B8A8_SNORM: 32,
    vk.VK_FORMAT_R8G8B8A8_USCALED: 32,
    vk.VK_FORMAT_R8G8B8A8_SSCALED: 32,
    vk.VK_FORMAT_R8G8B8A8_UINT: 32,
    vk.VK_FORMAT_R8G8B8A8_SINT: 32,
    vk.VK_FORMAT_R8G8B8A8_SRGB: 32,
    vk.VK_FORMAT_B8G8R8A8_UNORM: 32,
    vk.VK_FORMAT_B8G8R8A8_SNORM: 32,
    vk.VK_FORMAT_B8G8R8A8_USCALED: 32,
    vk.VK_FORMAT_B8G8R8A8_SSCALED: 32,
    vk.VK_FORMAT_B8G8R8A8_UINT: 32,
    vk.VK_FORMAT_B8G8R8A8_SINT: 32,
    vk.VK_FORMAT_B8G8R8A8_SRGB: 32,
    vk.VK_FORMAT_A8B8G8R8_UNORM_PACK32: 32,
    vk.VK_FORMAT_A8B8G8R8_SNORM_PACK32: 32,
    vk.VK_FORMAT_A8B8G8R8_USCALED_PACK32: 32,
    vk.VK_FORMAT_A8B8G8R8_SSCALED_PACK32: 32,
    vk.VK_FORMAT_A8B8G8R8_UINT_PACK32: 32,
    vk.VK_FORMAT_A8B8G8R8_SINT_PACK32: 32,
    vk.VK_FORMAT_A8B8G8R8_SRGB_PACK32: 32,
    vk.VK_FORMAT_A2R10G10B10_UNORM_PACK32: 32,
    vk.VK_FORMAT_A2R10G10B10_SNORM_PACK32: 32,
    vk.VK_FORMAT_A2R10G10B10_USCALED_PACK32: 32,
    vk.VK_FORMAT_A2R10G10B10_SSCALED_PACK32: 32,
    vk.VK_FORMAT_A2R10G10B10_UINT_PACK32: 32,
    vk.VK_FORMAT_A2R10G10B10_SINT_PACK32: 32,
    vk.VK_FORMAT_A2B10G10R10_UNORM_PACK32: 32,
    vk.VK_FORMAT_A2B10G10R10_SNORM_PACK32: 32,
    vk.VK_FORMAT_A2B10G10R10_USCALED_PACK32: 32,
    vk.VK_FORMAT_A2B10G10R10_SSCALED_PACK32: 32,
    vk.VK_FORMAT_A2B10G10R10_UINT_PACK32: 32,
    vk.VK_FORMAT_A2B10G10R10_SINT_PACK32: 32,
    vk.VK_FORMAT_R16_UNORM: 16,
    vk.VK_FORMAT_R16_SNORM: 16,
    vk.VK_FORMAT_R16_USCALED: 16,
    vk.VK_FORMAT_R16_SSCALED: 16,
    vk.VK_FORMAT_R16_UINT: 16,
    vk.VK_FORMAT_R16_SINT: 16,
    vk.VK_FORMAT_R16_SFLOAT: 16,
    vk.VK_FORMAT_R16G16_UNORM: 32,
    vk.VK_FORMAT_R16G16_SNORM: 32,
    vk.VK_FORMAT_R16G16_USCALED: 32,
    vk.VK_FORMAT_R16G16_SSCALED: 32,
    vk.VK_FORMAT_R16G16_UINT: 32,
    vk.VK_FORMAT_R16G16_SINT: 32,
    vk.VK_FORMAT_R16G16_SFLOAT: 32,
    vk.VK_FORMAT_R16G16B16_UNORM: 48,
    vk.VK_FORMAT_R16G16B16_SNORM: 48,
    vk.VK_FORMAT_R16G16B16_USCALED: 48,
    vk.VK_FORMAT_R16G16B16_SSCALED: 48,
    vk.VK_FORMAT_R16G16B16_UINT: 48,
    vk.VK_FORMAT_R16G16B16_SINT: 48,
    vk.VK_FORMAT_R16G16B16_SFLOAT: 48,
    vk.VK_FORMAT_R16G16B16A16_UNORM: 64,
    vk.VK_FORMAT_R16G16B16A16_SNORM: 64,
    vk.VK_FORMAT_R16G16B16A16_USCALED: 64,
    vk.VK_FORMAT_R16G16B16A16_SSCALED: 64,
    vk.VK_FORMAT_R16G16B16A16_UINT: 64,
    vk.VK_FORMAT_R16G16B16A16_SINT: 64,
    vk.VK_FORMAT_R16G16B16A16_SFLOAT: 64,
    vk.VK_FORMAT_R32_UINT: 32,
    vk.VK_FORMAT_R32_SINT: 32,
    vk.VK_FORMAT_R32_SFLOAT: 32,
    vk.VK_FORMAT_R32G32_UINT: 64,
    vk.VK_FORMAT_R32G32_SINT: 64,
    vk.VK_FORMAT_R32G32_SFLOAT: 64,
    vk.VK_FORMAT_R32G32B32_UINT: 96,
    vk.VK_FORMAT_R32G32B32_SINT: 96,
    vk.VK_FORMAT_R32G32B32_SFLOAT: 96,
    vk.VK_FORMAT_R32G32B32A32_UINT: 128,
    vk.VK_FORMAT_R32G32B32A32_SINT: 128,
    vk.VK_FORMAT_R32G32B32A32_SFLOAT: 128,
    vk.VK_FORMAT_R64_UINT: 64,
    vk.VK_FORMAT_R64_SINT: 64,
    vk.VK_FORMAT_R64_SFLOAT: 64,
    vk.VK_FORMAT_R64G64_UINT: 128,
    vk.VK_FORMAT_R64G64_SINT: 128,
    vk.VK_FORMAT_R64G64_SFLOAT: 128,
    vk.VK_FORMAT_R64G64B64_UINT: 194,
    vk.VK_FORMAT_R64G64B64_SINT: 194,
    vk.VK_FORMAT_R64G64B64_SFLOAT: 194,
    vk.VK_FORMAT_R64G64B64A64_UINT: 256,
    vk.VK_FORMAT_R64G64B64A64_SINT: 256,
    vk.VK_FORMAT_R64G64B64A64_SFLOAT: 256,
    vk.VK_FORMAT_B10G11R11_UFLOAT_PACK32: 32,
    vk.VK_FORMAT_E5B9G9R9_UFLOAT_PACK32: 32,
    vk.VK_FORMAT_D16_UNORM: 16,
    vk.VK_FORMAT_X8_D24_UNORM_PACK32: 32,
    vk.VK_FORMAT_D32_SFLOAT: 32,
    vk.VK_FORMAT_S8_UINT: 8,
    vk.VK_FORMAT_D16_UNORM_S8_UINT: 24,
    vk.VK_FORMAT_D24_UNORM_S8_UINT: 32,
    vk.VK_FORMAT_D32_SFLOAT_S8_UINT: 40,
    vk.VK_FORMAT_BC1_RGB_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC1_RGB_SRGB_BLOCK: 0,
    vk.VK_FORMAT_BC1_RGBA_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC1_RGBA_SRGB_BLOCK: 0,
    vk.VK_FORMAT_BC2_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC2_SRGB_BLOCK: 0,
    vk.VK_FORMAT_BC3_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC3_SRGB_BLOCK: 0,
    vk.VK_FORMAT_BC4_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC4_SNORM_BLOCK: 0,
    vk.VK_FORMAT_BC5_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC5_SNORM_BLOCK: 0,
    vk.VK_FORMAT_BC6H_UFLOAT_BLOCK: 0,
    vk.VK_FORMAT_BC6H_SFLOAT_BLOCK: 0,
    vk.VK_FORMAT_BC7_UNORM_BLOCK: 0,
    vk.VK_FORMAT_BC7_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ETC2_R8G8B8_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ETC2_R8G8B8_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK: 0,
    vk.VK_FORMAT_EAC_R11_UNORM_BLOCK: 0,
    vk.VK_FORMAT_EAC_R11_SNORM_BLOCK: 0,
    vk.VK_FORMAT_EAC_R11G11_UNORM_BLOCK: 0,
    vk.VK_FORMAT_EAC_R11G11_SNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_4x4_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_4x4_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_5x4_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_5x4_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_5x5_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_5x5_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_6x5_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_6x5_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_6x6_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_6x6_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_8x5_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_8x5_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_8x6_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_8x6_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_8x8_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_8x8_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x5_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x5_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x6_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x6_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x8_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x8_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x10_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_10x10_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_12x10_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_12x10_SRGB_BLOCK: 0,
    vk.VK_FORMAT_ASTC_12x12_UNORM_BLOCK: 0,
    vk.VK_FORMAT_ASTC_12x12_SRGB_BLOCK: 0,
    vk.VK_FORMAT_PVRTC1_2BPP_UNORM_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC1_4BPP_UNORM_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC2_2BPP_UNORM_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC2_4BPP_UNORM_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC1_2BPP_SRGB_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC1_4BPP_SRGB_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC2_2BPP_SRGB_BLOCK_IMG: 0,
    vk.VK_FORMAT_PVRTC2_4BPP_SRGB_BLOCK_IMG: 0,
}


# Mapping between layout value and its name
VK_LAYOUT_NAME = {}
for name in (
    'UNDEFINED', 'GENERAL', 'COLOR_ATTACHMENT_OPTIMAL',
    'DEPTH_STENCIL_ATTACHMENT_OPTIMAL', 'DEPTH_STENCIL_READ_ONLY_OPTIMAL',
    'SHADER_READ_ONLY_OPTIMAL', 'TRANSFER_SRC_OPTIMAL',
    'TRANSFER_DST_OPTIMAL', 'PREINITIALIZED', 'PRESENT_SRC_KHR'
):
    fn = 'VK_IMAGE_LAYOUT_%s' % name
    VK_LAYOUT_NAME[getattr(vk, fn)] = fn
