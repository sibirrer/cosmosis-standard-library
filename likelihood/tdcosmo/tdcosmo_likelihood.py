import os

def setup():
    """

    """
    # TODO: make file paths relative
    # 7 TDCOSMO lenses
    file = open(os.path.join(dir_path, 'tdcosmo7_likelihood_processed.pkl'), 'rb')
    tdcosmo7_likelihood_processed = pickle.load(file)
    file.close()

    # 33 SLACS lenses with SDSS spectroscopy
    file = open(os.path.join(dir_path, 'slacs_sdss_likelihood_processed.pkl'), 'rb')
    slacs_sdss_likelihood_processed = pickle.load(file)
    file.close()

    # 5 SLACS with IFU
    file = open(os.path.join(dir_path, 'slacs_ifu_likelihood_processed.pkl'), 'rb')
    slacs_ifu_likelihood_processed = pickle.load(file)
    file.close()


    `# import hierArc Likelihood class consistent with the arguments in the processed lenses
    from hierarc.Likelihood.lens_sample_likelihood import LensSampleLikelihood


    num_distribution_draws = 200  # number of draws from the hyper-parameter distribution in computing the Monte Carlo integral marginalization



    # here we update each individual lens likelihood configuration with the setting of the Monte-Carlo marginalization over hyper-parameter distributions
    for lens in tdcosmo7_likelihood_processed:
        lens['num_distribution_draws'] = num_distribution_draws
    for lens in slacs_sdss_likelihood_processed:
        lens['num_distribution_draws'] = num_distribution_draws
    for lens in slacs_ifu_likelihood_processed:
        lens['num_distribution_draws'] = num_distribution_draws


    # ====================
    # TDCOSMO 7 likelihood
    # ====================

    # hear we build a likelihood instance for the sample of 7 TDCOSMO lenses
    tdcosmo7_likelihood = LensSampleLikelihood(tdcosmo7_likelihood_processed)`

# here the additional parameters required to evaluate the likelihood in accordance with TDCOSMO IV Table 3

kwargs_lens_test = {'lambda_mst': 1.,  # mean in the internal MST distribution
                    'lambda_mst_sigma': 0.04,  # Gaussian sigma of the distribution of lambda_mst
                    'alpha_lambda': 0,  # slope of lambda_mst with r_eff/theta_E
                   }
kwargs_kin_test = {'a_ani': 1.5,  # mean a_ani anisotropy parameter in the OM model
                   'a_ani_sigma': 0.3,  # sigma(a_ani)⟨a_ani⟩ is the 1-sigam Gaussian scatter in a_ani
                  }

logl = tdcosmo7_likelihood.log_likelihood(cosmo=cosmo, kwargs_lens=kwargs_lens_test, kwargs_kin=kwargs_kin_test)

# TODO: make wrapper to translate cosmosis transverse angular diameter distance to CosmoInterp class that operates under hierArc conventions

from lenstronomy.Cosmo.cosmo_interp import CosmoInterp
cosmo = CosmoInterp(cosmo=cosmo, z_stop=self._z_max, num_interp=self._num_redshift_interp)

# TODO: hyper-parameter files and bounds



def execute(block, config):
    """

    """
    cosmo_astropy = cosmosis_cosmo_astropy_cosmo(block)


def cosmosis_cosmo_astropy_cosmo(cosmosis_cosmo):
    """

    :param cosmosis_cosmo: cosmosis cosmology object
    :return ~astropy.cosmology equivalent cosmology object
    """