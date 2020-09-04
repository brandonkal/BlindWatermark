import argparse
from BlindWatermark import watermark
from BlindWatermark import test_ncc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage="Embed or decode the blind watermark.", description="help info.")
    parser.add_argument("--key", '-k', default=(4399, 2333, 32), type=float,
                        help="Enter 2 random seeds and the divisor (positive number) in turn, the divisor can be one or two, separated by spaces.", dest="key", nargs='*')
    parser.add_argument('-d', '--dwt_deep', default=1, type=int,
                        help="Set the number of wavelet transforms, increasing the number of times will improve the robustness, but will reduce the ability of the image to carry watermarks, usually 1, 2, 3", dest="dwt_deep")
    parser.add_argument('-bs', '--block_shape', default=4, type=int,
                        help='Set the block size. Because the length and width are the same, you only need to pass an integer. For large images, you can use a larger number, such as 8. The larger shape makes the impact on the original image smaller, and The calculation time is reduced, but the robustness is not improved. Too much attention will cause the watermark information to exceed the carrying capacity of the picture', dest="block_shape")
    parser.add_argument('-em', '--embed', default=False,
                        action="store_true", dest="embed")
    parser.add_argument('-ex', '--extract', default=False,
                        action="store_true", dest="extract")
    parser.add_argument(
        "--read", '-r', help="The path of the picture to be embedded or extracted", dest="ori_img")
    parser.add_argument(
        "--read_wm", '-wm', help="The path of the watermark to be embedded", dest="wm")
    parser.add_argument("--wm_shape", '-ws', help="To solve the shape of the watermark",
                        dest="wm_shape", nargs=2)
    parser.add_argument("--out_put", '-o',
                        help="The output path of the picture", dest="output")
    parser.add_argument("--show_ncc", '-s', help="Show the NC value (similarity) between the output image and the original image",
                        default=False, action="store_true", dest="show_ncc")
    args = parser.parse_args()
    print(args)

    if (args.embed and args.extract) or ((not args.embed) and (not args.extract)):
        # args.embed and args.extract have and only one is True
        print("('-em','--embed') and ('-ex','--extract') must have one and only one")
        exit()
    elif args.embed:
        # Embedded watermark
        if len(args.key) == 3:
            random_seed1, random_seed2, mod1 = args.key
            bwm = watermark(int(random_seed1), int(random_seed2), mod1, block_shape=(
                args.block_shape, args.block_shape), dwt_deep=args.dwt_deep)
        elif len(args.key) == 4:
            random_seed1, random_seed2, mod1, mod2 = args.key
            bwm = watermark(int(random_seed1), int(random_seed2), mod1, mod2, block_shape=(
                args.block_shape, args.block_shape), dwt_deep=args.dwt_deep)
        else:
            print("You have entered {} keys, but this program only supports 3 or 4 keys".format(
                len(args.key)))
            exit()

        bwm.read_ori_img(args.ori_img)
        bwm.read_wm(args.wm)
        bwm.embed(args.output)
        if args.show_ncc:
            test_ncc(args.ori_img, args.output)

    elif args.extract:
        try:
            wm_shape0, wm_shape1 = args.wm_shape
            wm_shape0, wm_shape1 = int(wm_shape0), int(wm_shape1)
        except Exception as e:
            print("Input watermark shape", args.wm_shape, "did not qualify")
            print(e)
            exit()
        if len(args.key) == 3:
            random_seed1, random_seed2, mod1 = args.key
            bwm = watermark(int(random_seed1), int(random_seed2), mod1, wm_shape=(
                wm_shape0, wm_shape1), block_shape=(args.block_shape, args.block_shape), dwt_deep=args.dwt_deep)
        elif len(args.key) == 4:
            random_seed1, random_seed2, mod1, mod2 = args.key
            bwm = watermark(int(random_seed1), int(random_seed2), mod1, mod2, wm_shape=(
                wm_shape0, wm_shape1), block_shape=(args.block_shape, args.block_shape), dwt_deep=args.dwt_deep)
        bwm.extract(args.ori_img, args.output)
        if args.show_ncc:
            if args.wm:
                test_ncc(args.wm, args.output)
            else:
                print("When you want to show the similarity between the output watermark and the original watermark, you need to give the path of the original watermark")
