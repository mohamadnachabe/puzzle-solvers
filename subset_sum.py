def subset_sum(_set, _sum):
    def helper(set_, sum_, n):
        if not set_:
            return sum_ == 0 and n > 0

        return helper(set_[1:], sum_ - set_[0], n + 1) or helper(set_[1:], sum_, n)

    return helper(_set, _sum, 0)


if __name__ == '__main__':
    s = [-7, -2, -2, 4]
    print(subset_sum(s, 0))